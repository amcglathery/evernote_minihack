#
# Autogenerated by Thrift Compiler (0.8.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException
import evernote.edam.type.ttypes
import evernote.edam.error.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class SponsoredGroupRole(object):
  """
  Enumeration of Sponsored Group Roles
  """
  GROUP_MEMBER = 1
  GROUP_ADMIN = 2
  GROUP_OWNER = 3

  _VALUES_TO_NAMES = {
    1: "GROUP_MEMBER",
    2: "GROUP_ADMIN",
    3: "GROUP_OWNER",
  }

  _NAMES_TO_VALUES = {
    "GROUP_MEMBER": 1,
    "GROUP_ADMIN": 2,
    "GROUP_OWNER": 3,
  }


class PublicUserInfo(object):
  """
   This structure is used to provide publicly-available user information
   about a particular account.
  <dl>
   <dt>userId:</dt>
     <dd>
     The unique numeric user identifier for the user account.
     </dd>
   <dt>shardId:</dt>
     <dd>
     The name of the virtual server that manages the state of
     this user. This value is used internally to determine which system should
     service requests about this user's data.
     </dd>
   <dt>privilege:</dt>
     <dd>
     The privilege level of the account, to determine whether
     this is a Premium or Free account.
     </dd>
   <dt>noteStoreUrl:</dt>
     <dd>
     This field will contain the full URL that clients should use to make
     NoteStore requests to the server shard that contains that user's data.
     I.e. this is the URL that should be used to create the Thrift HTTP client
     transport to send messages to the NoteStore service for the account.
     </dd>
   </dl>

  Attributes:
   - userId
   - shardId
   - privilege
   - username
   - noteStoreUrl
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'userId', None, None, ), # 1
    (2, TType.STRING, 'shardId', None, None, ), # 2
    (3, TType.I32, 'privilege', None, None, ), # 3
    (4, TType.STRING, 'username', None, None, ), # 4
    (5, TType.STRING, 'noteStoreUrl', None, None, ), # 5
  )

  def __init__(self, userId=None, shardId=None, privilege=None, username=None, noteStoreUrl=None,):
    self.userId = userId
    self.shardId = shardId
    self.privilege = privilege
    self.username = username
    self.noteStoreUrl = noteStoreUrl

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.userId = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.shardId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.privilege = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.username = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.noteStoreUrl = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('PublicUserInfo')
    if self.userId is not None:
      oprot.writeFieldBegin('userId', TType.I32, 1)
      oprot.writeI32(self.userId)
      oprot.writeFieldEnd()
    if self.shardId is not None:
      oprot.writeFieldBegin('shardId', TType.STRING, 2)
      oprot.writeString(self.shardId)
      oprot.writeFieldEnd()
    if self.privilege is not None:
      oprot.writeFieldBegin('privilege', TType.I32, 3)
      oprot.writeI32(self.privilege)
      oprot.writeFieldEnd()
    if self.username is not None:
      oprot.writeFieldBegin('username', TType.STRING, 4)
      oprot.writeString(self.username)
      oprot.writeFieldEnd()
    if self.noteStoreUrl is not None:
      oprot.writeFieldBegin('noteStoreUrl', TType.STRING, 5)
      oprot.writeString(self.noteStoreUrl)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.userId is None:
      raise TProtocol.TProtocolException(message='Required field userId is unset!')
    if self.shardId is None:
      raise TProtocol.TProtocolException(message='Required field shardId is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class PremiumInfo(object):
  """
   This structure is used to provide information about a user's Premium account.
  <dl>
   <dt>currentTime:</dt>
     <dd>
     The server-side date and time when this data was generated.
     </dd>
   <dt>premium:</dt>
     <dd>
  	 True if the user's account is Premium.
     </dd>
   <dt>premiumRecurring</dt>
     <dd>
     True if the user's account is Premium and has a recurring payment method.
     </dd>
   <dt>premiumExpirationDate:</dt>
     <dd>
     The date when the user's Premium account expires, or the date when the
     user's account will be charged if it has a recurring payment method.
     </dd>
   <dt>premiumExtendable:</dt>
     <dd>
     True if the user is eligible for purchasing Premium account extensions.
     </dd>
   <dt>premiumPending:</dt>
     <dd>
     True if the user's Premium account is pending payment confirmation
     </dd>
   <dt>premiumCancellationPending:</dt>
     <dd>
     True if the user has requested that no further charges to be made; the
     Premium account will remain active until it expires.
     </dd>
   <dt>canPurchaseUploadAllowance:</dt>
     <dd>
     True if the user is eligible for purchasing additional upload allowance.
     </dd>
   <dt>sponsoredGroupName:</dt>
     <dd>
     The name of the sponsored group that the user is part of.
     </dd>
   <dt>sponsoredGroupRole:</dt>
     <dd>
     The role of the user within a sponsored group.
     </dd>
   </dl>

  Attributes:
   - currentTime
   - premium
   - premiumRecurring
   - premiumExpirationDate
   - premiumExtendable
   - premiumPending
   - premiumCancellationPending
   - canPurchaseUploadAllowance
   - sponsoredGroupName
   - sponsoredGroupRole
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'currentTime', None, None, ), # 1
    (2, TType.BOOL, 'premium', None, None, ), # 2
    (3, TType.BOOL, 'premiumRecurring', None, None, ), # 3
    (4, TType.I64, 'premiumExpirationDate', None, None, ), # 4
    (5, TType.BOOL, 'premiumExtendable', None, None, ), # 5
    (6, TType.BOOL, 'premiumPending', None, None, ), # 6
    (7, TType.BOOL, 'premiumCancellationPending', None, None, ), # 7
    (8, TType.BOOL, 'canPurchaseUploadAllowance', None, None, ), # 8
    (9, TType.STRING, 'sponsoredGroupName', None, None, ), # 9
    (10, TType.I32, 'sponsoredGroupRole', None, None, ), # 10
  )

  def __init__(self, currentTime=None, premium=None, premiumRecurring=None, premiumExpirationDate=None, premiumExtendable=None, premiumPending=None, premiumCancellationPending=None, canPurchaseUploadAllowance=None, sponsoredGroupName=None, sponsoredGroupRole=None,):
    self.currentTime = currentTime
    self.premium = premium
    self.premiumRecurring = premiumRecurring
    self.premiumExpirationDate = premiumExpirationDate
    self.premiumExtendable = premiumExtendable
    self.premiumPending = premiumPending
    self.premiumCancellationPending = premiumCancellationPending
    self.canPurchaseUploadAllowance = canPurchaseUploadAllowance
    self.sponsoredGroupName = sponsoredGroupName
    self.sponsoredGroupRole = sponsoredGroupRole

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.currentTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.premium = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.BOOL:
          self.premiumRecurring = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.premiumExpirationDate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.premiumExtendable = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BOOL:
          self.premiumPending = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.BOOL:
          self.premiumCancellationPending = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.BOOL:
          self.canPurchaseUploadAllowance = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.sponsoredGroupName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I32:
          self.sponsoredGroupRole = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('PremiumInfo')
    if self.currentTime is not None:
      oprot.writeFieldBegin('currentTime', TType.I64, 1)
      oprot.writeI64(self.currentTime)
      oprot.writeFieldEnd()
    if self.premium is not None:
      oprot.writeFieldBegin('premium', TType.BOOL, 2)
      oprot.writeBool(self.premium)
      oprot.writeFieldEnd()
    if self.premiumRecurring is not None:
      oprot.writeFieldBegin('premiumRecurring', TType.BOOL, 3)
      oprot.writeBool(self.premiumRecurring)
      oprot.writeFieldEnd()
    if self.premiumExpirationDate is not None:
      oprot.writeFieldBegin('premiumExpirationDate', TType.I64, 4)
      oprot.writeI64(self.premiumExpirationDate)
      oprot.writeFieldEnd()
    if self.premiumExtendable is not None:
      oprot.writeFieldBegin('premiumExtendable', TType.BOOL, 5)
      oprot.writeBool(self.premiumExtendable)
      oprot.writeFieldEnd()
    if self.premiumPending is not None:
      oprot.writeFieldBegin('premiumPending', TType.BOOL, 6)
      oprot.writeBool(self.premiumPending)
      oprot.writeFieldEnd()
    if self.premiumCancellationPending is not None:
      oprot.writeFieldBegin('premiumCancellationPending', TType.BOOL, 7)
      oprot.writeBool(self.premiumCancellationPending)
      oprot.writeFieldEnd()
    if self.canPurchaseUploadAllowance is not None:
      oprot.writeFieldBegin('canPurchaseUploadAllowance', TType.BOOL, 8)
      oprot.writeBool(self.canPurchaseUploadAllowance)
      oprot.writeFieldEnd()
    if self.sponsoredGroupName is not None:
      oprot.writeFieldBegin('sponsoredGroupName', TType.STRING, 9)
      oprot.writeString(self.sponsoredGroupName)
      oprot.writeFieldEnd()
    if self.sponsoredGroupRole is not None:
      oprot.writeFieldBegin('sponsoredGroupRole', TType.I32, 10)
      oprot.writeI32(self.sponsoredGroupRole)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.currentTime is None:
      raise TProtocol.TProtocolException(message='Required field currentTime is unset!')
    if self.premium is None:
      raise TProtocol.TProtocolException(message='Required field premium is unset!')
    if self.premiumRecurring is None:
      raise TProtocol.TProtocolException(message='Required field premiumRecurring is unset!')
    if self.premiumExtendable is None:
      raise TProtocol.TProtocolException(message='Required field premiumExtendable is unset!')
    if self.premiumPending is None:
      raise TProtocol.TProtocolException(message='Required field premiumPending is unset!')
    if self.premiumCancellationPending is None:
      raise TProtocol.TProtocolException(message='Required field premiumCancellationPending is unset!')
    if self.canPurchaseUploadAllowance is None:
      raise TProtocol.TProtocolException(message='Required field canPurchaseUploadAllowance is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AuthenticationResult(object):
  """
   When an authentication (or re-authentication) is performed, this structure
   provides the result to the client.
  <dl>
   <dt>currentTime:</dt>
     <dd>
     The server-side date and time when this result was
     generated.
     </dd>
   <dt>authenticationToken:</dt>
     <dd>
     Holds an opaque, ASCII-encoded token that can be
     used by the client to perform actions on a NoteStore.
     </dd>
   <dt>expiration:</dt>
     <dd>
     Holds the server-side date and time when the
     authentication token will expire.
     This time can be compared to "currentTime" to produce an expiration
     time that can be reconciled with the client's local clock.
     </dd>
   <dt>user:</dt>
     <dd>
     Holds the information about the account which was
     authenticated if this was a full authentication.  May be absent if this
     particular authentication did not require user information.
     </dd>
   <dt>publicUserInfo:</dt>
     <dd>
     If this authentication result was achieved without full permissions to
     access the full User structure, this field may be set to give back
     a more limited public set of data.
     </dd>
   <dt>noteStoreUrl:</dt>
     <dd>
     This field will contain the full URL that clients should use to make
     NoteStore requests to the server shard that contains that user's data.
     I.e. this is the URL that should be used to create the Thrift HTTP client
     transport to send messages to the NoteStore service for the account.
     </dd>
   <dt>webApiUrlPrefix:</dt>
     <dd>
     This field will contain the initial part of the URLs that should be used
     to make requests to Evernote's thin client "web API", which provide
     optimized operations for clients that aren't capable of manipulating
     the full contents of accounts via the full Thrift data model. Clients
     should concatenate the relative path for the various servlets onto the
     end of this string to construct the full URL, as documented on our
     developer web site.
     </dd>
   </dl>

  Attributes:
   - currentTime
   - authenticationToken
   - expiration
   - user
   - publicUserInfo
   - noteStoreUrl
   - webApiUrlPrefix
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'currentTime', None, None, ), # 1
    (2, TType.STRING, 'authenticationToken', None, None, ), # 2
    (3, TType.I64, 'expiration', None, None, ), # 3
    (4, TType.STRUCT, 'user', (evernote.edam.type.ttypes.User, evernote.edam.type.ttypes.User.thrift_spec), None, ), # 4
    (5, TType.STRUCT, 'publicUserInfo', (PublicUserInfo, PublicUserInfo.thrift_spec), None, ), # 5
    (6, TType.STRING, 'noteStoreUrl', None, None, ), # 6
    (7, TType.STRING, 'webApiUrlPrefix', None, None, ), # 7
  )

  def __init__(self, currentTime=None, authenticationToken=None, expiration=None, user=None, publicUserInfo=None, noteStoreUrl=None, webApiUrlPrefix=None,):
    self.currentTime = currentTime
    self.authenticationToken = authenticationToken
    self.expiration = expiration
    self.user = user
    self.publicUserInfo = publicUserInfo
    self.noteStoreUrl = noteStoreUrl
    self.webApiUrlPrefix = webApiUrlPrefix

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.currentTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.authenticationToken = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.expiration = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.user = evernote.edam.type.ttypes.User()
          self.user.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.publicUserInfo = PublicUserInfo()
          self.publicUserInfo.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.noteStoreUrl = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.webApiUrlPrefix = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AuthenticationResult')
    if self.currentTime is not None:
      oprot.writeFieldBegin('currentTime', TType.I64, 1)
      oprot.writeI64(self.currentTime)
      oprot.writeFieldEnd()
    if self.authenticationToken is not None:
      oprot.writeFieldBegin('authenticationToken', TType.STRING, 2)
      oprot.writeString(self.authenticationToken)
      oprot.writeFieldEnd()
    if self.expiration is not None:
      oprot.writeFieldBegin('expiration', TType.I64, 3)
      oprot.writeI64(self.expiration)
      oprot.writeFieldEnd()
    if self.user is not None:
      oprot.writeFieldBegin('user', TType.STRUCT, 4)
      self.user.write(oprot)
      oprot.writeFieldEnd()
    if self.publicUserInfo is not None:
      oprot.writeFieldBegin('publicUserInfo', TType.STRUCT, 5)
      self.publicUserInfo.write(oprot)
      oprot.writeFieldEnd()
    if self.noteStoreUrl is not None:
      oprot.writeFieldBegin('noteStoreUrl', TType.STRING, 6)
      oprot.writeString(self.noteStoreUrl)
      oprot.writeFieldEnd()
    if self.webApiUrlPrefix is not None:
      oprot.writeFieldBegin('webApiUrlPrefix', TType.STRING, 7)
      oprot.writeString(self.webApiUrlPrefix)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.currentTime is None:
      raise TProtocol.TProtocolException(message='Required field currentTime is unset!')
    if self.authenticationToken is None:
      raise TProtocol.TProtocolException(message='Required field authenticationToken is unset!')
    if self.expiration is None:
      raise TProtocol.TProtocolException(message='Required field expiration is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class BootstrapSettings(object):
  """
   This structure describes a collection of bootstrap settings.
  <dl>
   <dt>serviceHost:</dt>
     <dd>
     The hostname and optional port for composing Evernote web service URLs.
     This URL can be used to access the UserStore and related services,
     but must not be used to compose the NoteStore URL. Client applications
     must handle serviceHost values that include only the hostname
     (e.g. www.evernote.com) or both the hostname and port (e.g. www.evernote.com:8080).
     If no port is specified, or if port 443 is specified, client applications must
     use the scheme "https" when composing URLs. Otherwise, a client must use the
     scheme "http".
   </dd>
   <dt>marketingUrl:</dt>
     <dd>
     The URL stem for the Evernote corporate marketing website, e.g. http://www.evernote.com.
     This stem can be used to compose website URLs. For example, the URL of the Evernote
     Trunk is composed by appending "/about/trunk/" to the value of marketingUrl.
     </dd>
   <dt>supportUrl:</dt>
     <dd>
     The full URL for the Evernote customer support website, e.g. https://support.evernote.com.
     </dd>
   <dt>accountEmailDomain:</dt>
     <dd>
     The domain used for an Evernote user's incoming email address, which allows notes to
     be emailed into an account. E.g. m.evernote.com.
     </dd>
   <dt>enableFacebookSharing:</dt>
     <dd>
     Whether the client application should enable sharing of notes on Facebook.
     </dd>
   <dt>enableGiftSubscriptions:</dt>
     <dd>
     Whether the client application should enable gift subscriptions.
     </dd>
   <dt>enableSupportTickets:</dt>
     <dd>
     Whether the client application should enable in-client creation of support tickets.
     </dd>
   <dt>enableSharedNotebooks:</dt>
     <dd>
     Whether the client application should enable shared notebooks.
     </dd>
   <dt>enableSingleNoteSharing:</dt>
     <dd>
     Whether the client application should enable single note sharing.
     </dd>
   <dt>enableSponsoredAccounts:</dt>
     <dd>
     Whether the client application should enable sponsored accounts.
     </dd>
   <dt>enableTwitterSharing:</dt>
     <dd>
     Whether the client application should enable sharing of notes on Twitter.
     </dd>
   </dl>

  Attributes:
   - serviceHost
   - marketingUrl
   - supportUrl
   - accountEmailDomain
   - enableFacebookSharing
   - enableGiftSubscriptions
   - enableSupportTickets
   - enableSharedNotebooks
   - enableSingleNoteSharing
   - enableSponsoredAccounts
   - enableTwitterSharing
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'serviceHost', None, None, ), # 1
    (2, TType.STRING, 'marketingUrl', None, None, ), # 2
    (3, TType.STRING, 'supportUrl', None, None, ), # 3
    (4, TType.STRING, 'accountEmailDomain', None, None, ), # 4
    (5, TType.BOOL, 'enableFacebookSharing', None, None, ), # 5
    (6, TType.BOOL, 'enableGiftSubscriptions', None, None, ), # 6
    (7, TType.BOOL, 'enableSupportTickets', None, None, ), # 7
    (8, TType.BOOL, 'enableSharedNotebooks', None, None, ), # 8
    (9, TType.BOOL, 'enableSingleNoteSharing', None, None, ), # 9
    (10, TType.BOOL, 'enableSponsoredAccounts', None, None, ), # 10
    (11, TType.BOOL, 'enableTwitterSharing', None, None, ), # 11
  )

  def __init__(self, serviceHost=None, marketingUrl=None, supportUrl=None, accountEmailDomain=None, enableFacebookSharing=None, enableGiftSubscriptions=None, enableSupportTickets=None, enableSharedNotebooks=None, enableSingleNoteSharing=None, enableSponsoredAccounts=None, enableTwitterSharing=None,):
    self.serviceHost = serviceHost
    self.marketingUrl = marketingUrl
    self.supportUrl = supportUrl
    self.accountEmailDomain = accountEmailDomain
    self.enableFacebookSharing = enableFacebookSharing
    self.enableGiftSubscriptions = enableGiftSubscriptions
    self.enableSupportTickets = enableSupportTickets
    self.enableSharedNotebooks = enableSharedNotebooks
    self.enableSingleNoteSharing = enableSingleNoteSharing
    self.enableSponsoredAccounts = enableSponsoredAccounts
    self.enableTwitterSharing = enableTwitterSharing

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.serviceHost = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.marketingUrl = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.supportUrl = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.accountEmailDomain = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.enableFacebookSharing = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BOOL:
          self.enableGiftSubscriptions = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.BOOL:
          self.enableSupportTickets = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.BOOL:
          self.enableSharedNotebooks = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.BOOL:
          self.enableSingleNoteSharing = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.BOOL:
          self.enableSponsoredAccounts = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.BOOL:
          self.enableTwitterSharing = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('BootstrapSettings')
    if self.serviceHost is not None:
      oprot.writeFieldBegin('serviceHost', TType.STRING, 1)
      oprot.writeString(self.serviceHost)
      oprot.writeFieldEnd()
    if self.marketingUrl is not None:
      oprot.writeFieldBegin('marketingUrl', TType.STRING, 2)
      oprot.writeString(self.marketingUrl)
      oprot.writeFieldEnd()
    if self.supportUrl is not None:
      oprot.writeFieldBegin('supportUrl', TType.STRING, 3)
      oprot.writeString(self.supportUrl)
      oprot.writeFieldEnd()
    if self.accountEmailDomain is not None:
      oprot.writeFieldBegin('accountEmailDomain', TType.STRING, 4)
      oprot.writeString(self.accountEmailDomain)
      oprot.writeFieldEnd()
    if self.enableFacebookSharing is not None:
      oprot.writeFieldBegin('enableFacebookSharing', TType.BOOL, 5)
      oprot.writeBool(self.enableFacebookSharing)
      oprot.writeFieldEnd()
    if self.enableGiftSubscriptions is not None:
      oprot.writeFieldBegin('enableGiftSubscriptions', TType.BOOL, 6)
      oprot.writeBool(self.enableGiftSubscriptions)
      oprot.writeFieldEnd()
    if self.enableSupportTickets is not None:
      oprot.writeFieldBegin('enableSupportTickets', TType.BOOL, 7)
      oprot.writeBool(self.enableSupportTickets)
      oprot.writeFieldEnd()
    if self.enableSharedNotebooks is not None:
      oprot.writeFieldBegin('enableSharedNotebooks', TType.BOOL, 8)
      oprot.writeBool(self.enableSharedNotebooks)
      oprot.writeFieldEnd()
    if self.enableSingleNoteSharing is not None:
      oprot.writeFieldBegin('enableSingleNoteSharing', TType.BOOL, 9)
      oprot.writeBool(self.enableSingleNoteSharing)
      oprot.writeFieldEnd()
    if self.enableSponsoredAccounts is not None:
      oprot.writeFieldBegin('enableSponsoredAccounts', TType.BOOL, 10)
      oprot.writeBool(self.enableSponsoredAccounts)
      oprot.writeFieldEnd()
    if self.enableTwitterSharing is not None:
      oprot.writeFieldBegin('enableTwitterSharing', TType.BOOL, 11)
      oprot.writeBool(self.enableTwitterSharing)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.serviceHost is None:
      raise TProtocol.TProtocolException(message='Required field serviceHost is unset!')
    if self.marketingUrl is None:
      raise TProtocol.TProtocolException(message='Required field marketingUrl is unset!')
    if self.supportUrl is None:
      raise TProtocol.TProtocolException(message='Required field supportUrl is unset!')
    if self.accountEmailDomain is None:
      raise TProtocol.TProtocolException(message='Required field accountEmailDomain is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class BootstrapProfile(object):
  """
   This structure describes a collection of bootstrap settings.
  <dl>
   <dt>name:</dt>
     <dd>
     The unique name of the profile, which is guaranteed to remain consistent across
     calls to getBootstrapInfo.
     </dd>
   <dt>settings:</dt>
     <dd>
     The settings for this profile.
     </dd>
   </dl>

  Attributes:
   - name
   - settings
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRUCT, 'settings', (BootstrapSettings, BootstrapSettings.thrift_spec), None, ), # 2
  )

  def __init__(self, name=None, settings=None,):
    self.name = name
    self.settings = settings

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.settings = BootstrapSettings()
          self.settings.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('BootstrapProfile')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.settings is not None:
      oprot.writeFieldBegin('settings', TType.STRUCT, 2)
      self.settings.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    if self.settings is None:
      raise TProtocol.TProtocolException(message='Required field settings is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class BootstrapInfo(object):
  """
   This structure describes a collection of bootstrap profiles.
  <dl>
   <dt>profiles:</dt>
     <dd>
     List of one or more bootstrap profiles, in descending
     preference order.
     </dd>
   </dl>

  Attributes:
   - profiles
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'profiles', (TType.STRUCT,(BootstrapProfile, BootstrapProfile.thrift_spec)), None, ), # 1
  )

  def __init__(self, profiles=None,):
    self.profiles = profiles

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.profiles = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = BootstrapProfile()
            _elem5.read(iprot)
            self.profiles.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('BootstrapInfo')
    if self.profiles is not None:
      oprot.writeFieldBegin('profiles', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.profiles))
      for iter6 in self.profiles:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.profiles is None:
      raise TProtocol.TProtocolException(message='Required field profiles is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
