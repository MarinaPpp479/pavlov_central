import connexion
from connexion import NoContent
from pavlov_central.api.helper.api_helper import merge_dict
from pavlov_central.storage.models.player import Player
from pavlov_central.api.models.player import Player as PlayerApi


def handle_get_player_list():
    #return Player.select().dicts()[:]
    player_api_list = []
    for player in Player.select().dicts()[:]:
        player_api_list.append(PlayerApi.from_dict(player))
    return player_api_list
