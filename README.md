# Apollo Federation Mutation Demo


This repository is a demonstration of using Apollo Federation with the Python library [Strawberry-GraphQL](https://strawberry.rocks/) for handling mutation that access data from external services/subgraphs.

```graphql
type ReviewMutation @key(fields: "productId") {
  productId: String!
  product: Product @external
  currentUser: User @external
  comment(body: String!): Review! @requires(fields: "product{upc} currentUser{id}")
}

type Mutation {
  review(productId: String!): ReviewMutation!
}
```

Included in the project is an example mutation, `comment`, that demonstrates how to fetch data from external services (*product.upc* from the products subgraph and *currentUser.id* from the accounts subgraph) in order to ensure consistency of the review.

Note that this approach requires the external key (such as productId) to be provided earlier in the mutation rather than packed into a single input type.

An example mutation query is provided for reference.


```graphql
mutation ExampleMutation($productId: String!, $body: String!) {
  review(productId: $productId){
    comment(body: $body) {
      ...
    }
  }
}
```

# Setup
1. Clone the repository
2. Start the services: `docker-compose up`
3. Access the sandbox at `http://localhost:4000`
4. [Optional] View a full example at [this share link](http://localhost:4000/?explorerURLState=N4IgJg9gxgrgtgUwHYBcQC4RxighigSwiQAIAZCAcwKQAoASGAZwQCcldF0SBlFVmpQCEAShLAAOqRIAbKjVrM2HLiUYt2nBGMnSSJAmCn79KhMZNLNiCwF8p9pFKkBHGGwCeJWK1bIUAKoa4haIIXoGRhFmFvpWMdKOjs5I2HiExCQAogAenAAOMggAsjj4RHT0%2BawQYDBQKACSYNx8AkjCADRqAEa1Hq38gqLh%2Bn4AbgQIAO601bX1TS1q83UNzSK6Jt4QcIiotH1gA739OrEmhhf6Rx7XJKuLo9smCS8mE1PTTM-v%2Brg4AAWEFYvz%2Bpi0922jnBN36UJIMJeSP0SKSIE6IHGuAEuB6RSYGBAWxIEhAtzJ3DJSAgKBIPVwYCEZM6FjJj3WRgwpJAAEYWWyQPFIdyyQABRm4AVIWwgWxAA)

Note: If you make any changes to Strawberry's schema, please run `bash ./apollo-router/supergraph_compose.sh` to update the `*.graphql` files.



---

For reference, the implementation of the `ReviewMutation` can be found in the following files:

- orders subgraph:
  - https://github.com/filwaline/Apollo-Federation-Mutation-Demo/blob/main/services/reviews/reviews/graphql.py#L17-L29
  - https://github.com/filwaline/Apollo-Federation-Mutation-Demo/blob/main/services/reviews/reviews/graphql.py#L39-L52
- accounts subgraph:
  - https://github.com/filwaline/Apollo-Federation-Mutation-Demo/blob/main/services/accounts/accounts/stubs.py#L7-L16
- products subgraph:
  - https://github.com/filwaline/Apollo-Federation-Mutation-Demo/blob/main/services/products/products/stubs.py#L7-L16

Please take a look at the above links for more information about how the code works.


