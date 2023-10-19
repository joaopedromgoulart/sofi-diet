from typing import List
from app.controller.data_source.users import Pasciente, UsersService
from app.model.data_conn.postgress import PostgressConn


class UsersPostgressConn(UsersService, PostgressConn):
    def list_passientes(self, nutri_id: str) -> List[Pasciente]:
        # inicia conexao com banco de dados
        # Faz a query
        # estrutura os dados
        return # retorna no padrao esperado