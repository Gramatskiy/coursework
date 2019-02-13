<template>
    <v-flex xs12 row class="d-flex flex-wrap">
        <h1 class="w-100 text-xs-center">{{t("Amount dynamics")}}</h1>


        <chart :chartData="prepareChartData" :options="{responsive: true, maintainAspectRatio: true}"
               :height="150"></chart>
    </v-flex>
</template>

<script>
    import Chart from './Chart'
    import AdminApi from './api'

    export default {
        name: 'ProductAmountStatistics',
        components: {Chart},
        props: ['id'],
        data() {
            return {
                productAmountList: []
            }
        },
        created() {
            AdminApi.getProductAmountList({id: this.id})
                .then(response => this.productAmountList = response.data)
        },
        computed: {
            prepareChartData() {
                const labels = this.productAmountList.map(i => this.$moment(i.timestamp).format("LLL"));
                return {
                    labels,
                    datasets: [{
                        label: this.$translate.text("Amount dynamics"),
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        data: this.productAmountList.map(p => p.amount)
                    }]
                }
            }
        }
    }
</script>

<style scoped>

</style>
