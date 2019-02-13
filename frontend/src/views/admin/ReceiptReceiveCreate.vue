<template>
    <v-flex v-if="products.length > 0" xs12 row class="d-flex flex-wrap">
        <h1 class="w-100 text-xs-center">{{t("Create received receipt")}}</h1>
        <v-flex v-for="product in products" class="d-flex w-25  pa-1" :key="product.id">
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
                        </div>
                    </v-card-title>
                    <v-card-actions>
                        <v-btn flat color="success" @click="createReceiveInvoice(product.id)">
                            {{t("Create received receipt")}}
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
        name: 'ReceiptReceiveCreate',
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
            createReceiveInvoice(productId) {
                AdminApi.createReceiptReceive({fields: {'product': productId}})
                    .then(() => {
                        alert(this.$translate.text("Receive receipt has been created"))
                    })
            }
        }
    }
</script>

<style scoped>

</style>
