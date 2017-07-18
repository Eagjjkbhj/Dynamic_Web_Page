import server
'''
#a = input()
def home(request, response):
  return server.send_html_handler(request, response,'hello')
  
def homesam(request, response):
  return server.send_html_handler(request, response, request["path"])

abc = {"A : amma","B: baba"}

def get_handler_test(request, response):
    """HTTP GET Handler"""
    try:
    	if server.ROUTES["get"][request["path"]](request, response) is None:
    		server.add_route('get',request["path"],request["path"])
    		return ROUTES["get"][request["path"]](request, response)
    except KeyError:
        return static_file_handler(request, response)
'''
#server.add_route('get', '/', home)
#server.add_route('get', request["path"], homesam)
#server.add_route('get', a, homesam)
#print(server.get_header(abc))
#print(server.ROUTES)
server.start_server("localhost", 8080)





