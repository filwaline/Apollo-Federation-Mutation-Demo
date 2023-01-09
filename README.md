# Apollo-Federation-Mutation-Demo


This repository is a demo of apollo federation, focus on **federated mutation** over multiple services.

**federated mutation** is a mutation that can fetch data from external services(handle by apollo-router), rather than execute mutation distribute over mulpitle services.

```graphql
type ReviewMutation @key(fields: "productId") {
  productId: String!
  product: Product @external
  currentUser: User @external
  comment(body: String!): Review! @requires(fields: "product{upc} currentUser{id}")
}
```
`comment` is a mutation that can fetch product.upc(from products subgarph) and currentUser.id(from accounts subgraph), so `comment` won't create a inconsistent review.


---

You may run this project with `docker compose up` and landing sandbox at `http://localhost:4000`

This project written with python libary [strawberry-graphql](https://strawberry.rocks/)

If you make any changes to strawberry's schema, please run `bash ./apollo-router/supergraph_compose.sh` to update *.graphql files.
