from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
  # Just HTTP for now. (We can add other protocols later.)
})
