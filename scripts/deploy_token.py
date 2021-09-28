from scripts.helper_script import get_account
from brownie import OurToken, config, network
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")  # the initial supply value


def deploy_token():
    account = get_account()
    our_token = OurToken.deploy(
        initial_supply, {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False))


def main():
    deploy_token()
