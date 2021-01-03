# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=no-member
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import notes.routing

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
    URLRouter(
      notes.routing.websocket_urlpatterns
    )
  )
})
