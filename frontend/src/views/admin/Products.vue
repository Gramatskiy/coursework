<template>
    <v-flex v-if="products.length > 0" xs12 row class="d-flex flex-wrap">
        <h1 class="w-100 text-xs-center">{{t("Your products")}}</h1>
        <butto
        <v-flex v-for="product in products" xs6 class="d-flex w-25  pa-1" :key="product.id">
            <v-card>
                <v-img
                        :src="product.photo"
                        aspect-ratio="1.5"
                ></v-img>
                <template>
                    <v-card-title primary-title>
                        <div>
                            <v-layout row align-center>
                                <h2 class="headline mb-0">{{product.name}}</h2>
                            </v-layout>
                            <h4>{{product.description}}</h4>
                            <div>{{t("Amount is")}} {{product.amount.amount}}</div>
                        </div>
                    </v-card-title>
                    <v-card-actions>
                        <v-btn flat color="success"
                               @click="$router.push({'name':'admin-product-update', 'params':{'id':product.id}})">
                            {{t("Update")}}
                        </v-btn>
                        <v-btn flat color="error"
                               @click="deleteProduct(product)">
                            {{t("Remove")}}
                        </v-btn>
                    </v-card-actions>
                </template>
            </v-card>
        </v-flex>
    </v-flex>
</template>

<script>
    import AdminApi from './api'

    export default {
        name: 'Products',
        data() {
            return {
                products: []
            }
        },
        created() {
            this.getProductList();
        },
        methods: {
            getProductList() {
                AdminApi.getProductList({})
                    .then(response => {
                        this.products = response.data
                    })
                    .catch(reason => console.error(reason.response || reason))
            },
            deleteProduct(product) {
                const confirmation = confirm(this.$translate.text("Are you sure to delete the product:") + " " + product.name)
                if (confirmation) {
                    AdminApi.deleteProduct({id: product.id})
                        .then(() => this.getProductList())
                        .catch(reason => console.error(reason.response || reason))
                }
            }
        }
    }
</script>

<style scoped>
    .flex-wrap {
        flex-wrap: wrap;
    }

    .w-100 {
        width: 100%;
    }

    .w-50 {
        width: 50%;
    }

    .w-25 {
        width: 25%;
    }
</style>
