<template>
    <v-layout align-center justify-center>
        <v-flex xs12 sm6>
            <v-form ref="form" @submit.prevent="createProduct">
                <v-text-field
                        v-model="name"
                        :label="t('Name')"
                        required
                ></v-text-field>
                <v-text-field
                        v-model="description"
                        :label="t('Description')"
                ></v-text-field>
                <label>{{t("Photo")}}
                    <input type="file" id="photo" ref="photo" v-on:change="handleFileUpload()"/>
                </label>
                <v-text-field
                        v-model="amount"
                        :label="t('Amount')"
                ></v-text-field>
                <v-layout justify-space-between>
                    <v-btn color="success" type="submit">{{t('Add')}}</v-btn>
                </v-layout>
            </v-form>
        </v-flex>
    </v-layout>
</template>

<script>
    import AdminApi from './api'

    export default {
        name: 'CreateProduct',

        data() {
            return {
                name: null,
                description: null,
                amount: 1,
                photo: null,
            }
        },
        methods: {
            createProduct() {
                let formData = new FormData();
                if (this.photo) {
                    formData.append('photo', this.photo);
                }
                if (this.amount) {
                    formData.append('amount', this.amount)
                }
                formData.append('name', this.name);
                formData.append('description', this.description);
                AdminApi.createProduct({id: this.id, fields: formData})
                    .then(() => this.$router.push({'name': 'admin-products'}))
            }
            ,
            handleFileUpload() {
                this.photo = this.$refs.photo.files[0];
            }
        }
    }
</script>

<style scoped>

</style>
