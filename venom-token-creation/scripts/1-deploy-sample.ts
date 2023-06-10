import { Address, getRandomNonce, toNano } from "locklift";

async function main() {
  const json = {
    "type": "Basic NFT",
    "name": "Venom Hackathon POAP",
    "description": "POAP for Venom Hackathon",
    "preview": {
      "source": "https://cdn.dorahacks.io/static/files/187b78231e813c1d200a83f4996aae33.jpg",
      "mimetype": "image/png"
    },
    "files": [
      {
        "source": "https://cdn.dorahacks.io/static/files/187b78231e813c1d200a83f4996aae33.jpg",
        "mimetype": "image/jpg"
      }
    ],
    "external_url": "https://google.com"
  };
  const signer = (await locklift.keystore.getSigner("0"))!;
  const nft = locklift.factory.getContractArtifacts("Nft");
  const index = locklift.factory.getContractArtifacts("Index");
  const indexBasis = locklift.factory.getContractArtifacts("IndexBasis");
  const { contract: sample, tx } = await locklift.factory.deployContract({
    contract: "Sample",
    publicKey: signer.publicKey,
    initParams: {
      nonce: getRandomNonce(),
      owner: `0x${signer.publicKey}`,
    },
    constructorParams: {
      _state: 0,
      root_: new Address("0:3eb450ea8e4a9bacc46fdd733caaa156edb8be82113469dae234ca6f8907e258"),
      json: JSON.stringify(json),
      codeNft: nft.code,
      codeIndex: index.code,
      codeIndexBasis: indexBasis.code
    },
    value: locklift.utils.toNano(3),
  });
  console.log(`Sample deployed at: ${sample.address.toString()}`);
}

main()
  .then(() => process.exit(0))
  .catch(e => {
    console.log(e);
    process.exit(1);
  });
