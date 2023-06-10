import { Address, toNano, WalletTypes } from "locklift";

async function main(name, symbol, initialSupply) {
  console.log("Name: ", name);
  console.log("Symbol: ", symbol);
  console.log("initialSupply: ", initialSupply);
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
      name_: name,
      symbol_: symbol,
      decimals_: 9,
      rootOwner_: new Address("0:3eb450ea8e4a9bacc46fdd733caaa156edb8be82113469dae234ca6f8907e258"),
      walletCode_: (await locklift.factory.getContractArtifacts("TokenWallet")).code,
      deployer_: new Address("0:0000000000000000000000000000000000000000000000000000000000000000"),
    },
    constructorParams: {
      initialSupplyTo: new Address("0:3eb450ea8e4a9bacc46fdd733caaa156edb8be82113469dae234ca6f8907e258"),
      initialSupply: initialSupply,
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

// Retrieve the command line arguments
const [name, symbol, initialSupply] = process.argv.slice(5);

main(name, symbol, parseInt(initialSupply))
  .then(() => process.exit(0))
  .catch(e => {
    console.log(e);
    process.exit(1);
  });