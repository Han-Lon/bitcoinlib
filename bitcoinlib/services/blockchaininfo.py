# -*- coding: utf-8 -*-
#
#    BitcoinLib - Python Cryptocurrency Library
#    blockchain_info client
#    © 2016 November - 1200 Web Development <http://1200wd.com/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from bitcoinlib.services.baseclient import BaseClient

PROVIDERNAME = 'blockchaininfo'


class BlockchainInfoClient(BaseClient):

    def __init__(self, network, base_url, denominator, api_key=''):
        super(self.__class__, self).__init__(network, PROVIDERNAME, base_url, denominator, api_key)

    def compose_request(self, cmd, parameter, variables=None, method='get'):
        url_path = cmd
        if parameter:
            url_path += '/' + parameter
        return self.request(url_path, variables, method=method)

    def getbalance(self, addresslist):
        variables = [('active', '|'.join(addresslist))]
        res = self.compose_request('multiaddr', '', variables)
        balance = 0
        for address in res['addresses']:
            balance += address['final_balance']

        return balance

    def getrawtransaction(self, txid):
        # https://blockchain.info/rawtx/$tx_hash
        res = self.compose_request('rawtx', txid, {'format': 'hex'})
        return res

    # def decoderawtransaction(self, rawtx):
    #     return self.compose_request('tx', 'decode', variables={'hex': rawtx}, method='post')
    #
    # def sendrawtransaction(self, rawtx):
    #     return self.compose_request('tx', 'push', variables={'hex': rawtx}, method='post')
