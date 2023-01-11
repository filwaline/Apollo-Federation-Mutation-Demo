# Apollo Federation Mutation Demo


This repository is a demo of apollo federation, focus on **federated mutation** over multiple services.

**federated mutation** is a mutation that can fetch data from external services(handle by apollo-router), rather than execute mutation distribute over mulpitle services.

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
`comment` is a mutation that can fetch product.upc(from products subgarph) and currentUser.id(from accounts subgraph), so `comment` won't create a inconsistent review.

And the price is, you will have to provide external key (such as `productId`) early, rather then pack them into a single input type of `comment`.

```graphql
mutation ExampleMutation($productId: String!, $body: String!) {
  review(productId: $productId){
    comment(body: $body) {
      ...
    }
  }
}
```

---

You may run this project with `docker compose up` and landing sandbox at `http://localhost:4000`

This project written with python libary [strawberry-graphql](https://strawberry.rocks/)

If you make any changes to strawberry's schema, please run `bash ./apollo-router/supergraph_compose.sh` to update *.graphql files.


---

`ReviewMutation` Reference:
  - orders subgraph
    - https://github.com/filwaline/Apollo-Federation-Mutation-Demo/blob/main/services/reviews/reviews/graphql.py#L19-L35
    - https://github.com/filwaline/Apollo-Federation-Mutation-Demo/blob/main/services/reviews/reviews/graphql.py#L45-L62
  - accounts subgraph
    - https://github.com/filwaline/Apollo-Federation-Mutation-Demo/blob/main/services/accounts/accounts/stubs.py#L9-L15
  - products subgraph
    - https://github.com/filwaline/Apollo-Federation-Mutation-Demo/blob/main/services/products/products/stubs.py#L9-L17
