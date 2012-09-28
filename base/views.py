from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from evernote_auth import EvernoteAPI
from account.models import UserProfile
import thrift.protocol.TBinaryProtocol as TBinaryProtocol
import thrift.transport.THttpClient as THttpClient


def index(request):
    return render_to_response('base.html', {},
                              context_instance=RequestContext(request))

def run_evernote_auth(request):
    """ Starts the OAuth token obtaining process by obtaining the token we use
        to request the user's token
    """
    callback_url = request.build_absolute_uri(reverse(
        'base.views.login_evernote_token', args=[]))

    everAuth = EvernoteAPI()
    return everAuth.get_token(request, callback_url)

def login_evernote_token(request):
    """ as get_evernote_token(), but logs the user in as well
    """
    everAuth = EvernoteAPI()
    credentials = everAuth.get_user_token(request)
    if not credentials:
        return HttpResponseRedirect(reverse('account.views.login_page', args=[]))
    if request.user.is_authenticated():
        user = request.user
    else:
        evernoteHost = settings.EVERNOTE_HOST
        userStoreUri = "https://" + evernoteHost + "/edam/user"
        userStoreHttpClient = THttpClient.THttpClient(userStoreUri)
        userStoreProtocol = TBinaryProtocol.TBinaryProtocol(userStoreHttpClient)
        userStore = UserStore.Client(userStoreProtocol)
        evernoteUser = userStore.getUser(credentials['oauth_token'])
        user = authenticate(username=evernoteUser.username, password=str(evernoteUser.id))
        if not user:
            newUser = User.objects.create_user(evernoteUser.username, evernoteUser.email, str(evernoteUser.id))
            names = evernoteUser.name.split() if evernoteUser.name else None
            newUser.first_name = names[0] if names and len(names) > 0 else ""
            newUser.last_name = names[1] if names and len(names) > 1 else ""
            newUser.save()
            user = authenticate(username=evernoteUser.username, password=str(evernoteUser.id))
        login(request, user)
    profile = request.user.profile
    try:
        expires_time = datetime.fromtimestamp(int(credentials['expires']))
    except TypeError:
        logging.error("Error parsing token expires time")
        expires_time = datetime.now()
    profile.evernote_token = credentials['oauth_token']
    profile.evernote_token_expires_time = expires_time
    profile.evernote_note_store_url = credentials['edam_noteStoreUrl']
    profile.save()
    return HttpResponseRedirect(reverse('basic.views.index',
        args=[]))
