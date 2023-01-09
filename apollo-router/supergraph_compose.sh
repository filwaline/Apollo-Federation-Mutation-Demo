#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SUBGRAPHS_LOCATION="$SCRIPT_DIR/subgraphs"

declare -a apps=(
    "accounts"
    "inventory"
    "products"
    "reviews"
)

for name in "${apps[@]}"
do
    strawberry export-schema "$name.main:schema" > "$SUBGRAPHS_LOCATION/$name.graphql"
done


if ! [ -x "$(command -v rover)" ]; then
    echo "'rover' could not be found, auto installing..."
    curl -sSL https://rover.apollo.dev/nix/latest | sh
fi

rover supergraph compose \
    --elv2-license accept \
    --skip-update \
    --config "$SCRIPT_DIR/supergraph.yaml" \
    > "$SCRIPT_DIR/supergraph.graphql"
