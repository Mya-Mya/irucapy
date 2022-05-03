from mytesttool import testerfunc
import irucapy

@testerfunc
def get_room_member():
    print("Valid ROOM-CODE")
    api = irucapy.api.httpirucaapi.HTTPIrucaAPI()
    room = api.get_room_info(input("ROOM-CODE: "))
    print(room)

get_room_member()