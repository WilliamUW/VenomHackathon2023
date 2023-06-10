import { Address, toNano, WalletTypes } from "locklift";

async function main() {
  const signer = (await locklift.keystore.getSigner("0"))!;
  const { account } = await locklift.factory.accounts.addNewAccount({
    type: WalletTypes.WalletV3,
    value: toNano(100000),
    publicKey: signer.publicKey,
  });
  const { contract: tokenRoot, tx } = await locklift.factory.deployContract({
    contract: "TokenRoot",
    publicKey: signer.publicKey,
    initParams: {
      randomNonce_: 0,
      name_: "VenomChat Token 2",
      symbol_: "VCHAT 2",
      decimals_: 9,
      rootOwner_: new Address("0:3eb450ea8e4a9bacc46fdd733caaa156edb8be82113469dae234ca6f8907e258"),
      walletCode_: (await locklift.factory.getContractArtifacts("TokenWallet")).code,
      deployer_: new Address("0:0000000000000000000000000000000000000000000000000000000000000000"),
    },
    constructorParams: {
      initialSupplyTo: new Address("0:3eb450ea8e4a9bacc46fdd733caaa156edb8be82113469dae234ca6f8907e258"),
      initialSupply: 100000000000,
      deployWalletValue: 100000000,
      mintDisabled: true,
      burnByRootDisabled: true,
      burnPaused: false,
      remainingGasTo: account.address,
  },
    value: locklift.utils.toNano(2),
  });

  console.log(`TokenRoot deployed at: ${tokenRoot.address.toString()}`);
}

main()
  .then(() => process.exit(0))
  .catch(e => {
    console.log(e);
    process.exit(1);
  });
