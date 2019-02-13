<template>
    <v-flex v-if="receipts.length > 0" xs12 row class="d-flex flex-wrap">
        <h1 class="w-100 text-xs-center">{{t("Sold receipts")}}</h1>
        <v-flex v-for="receipt in receipts" class="d-flex w-25  pa-1" :key="receipt.id">
            <v-card>
                <v-img
                        :src="receipt.product.photo"
                        aspect-ratio="1.5"
                ></v-img>
                <template>
                    <v-card-title primary-title>
                        <div>
                            <v-layout row align-center class="justify-space-between">
                                <h2 class="headline mb-0">{{receipt.product.name}}</h2>
                                <div class="ml-2 grey--text">({{receipt.timestamp|moment('LLL')}})
                                </div>
                            </v-layout>
                        </div>
                    </v-card-title>
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
                receipts: []
            }
        },
        created() {
            this.getProductList();
        },
        methods: {
            getProductList() {
                AdminApi.getReceiptSellList({})
                    .then(response => {
                        this.receipts = response.data
                    })
                    .catch(reason => console.error(reason.response || reason))
            },
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
