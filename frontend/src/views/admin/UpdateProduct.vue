<template>
    <v-layout align-center justify-center>
        <v-flex xs12 sm6>
            <v-form ref="form" @submit.prevent="updateProduct" v-if="name">
                <v-text-field
                        v-model="name"
                        :label="t('Name')"
                        required
                ></v-text-field>
                <v-text-field
                        v-model="description"
                        :label="t('Description')"
                ></v-text-field>
                <v-img
                        :src="currentPhoto"
                        aspect-ratio="1.5"
                ></v-img>
                <label>{{t("Photo")}}
                    <input type="file" id="photo" ref="photo" v-on:change="handleFileUpload()"/>
                </label>
                <v-text-field
                        v-model="amount"
                        :label="t('Amount')"
                ></v-text-field>
                <v-layout justify-space-between>
                    <v-btn color="success" type="submit">{{t('Update')}}</v-btn>
                </v-layout>
            </v-form>
        </v-flex>
    </v-layout>
</template>

<script>
    import AdminApi from './api'


    export default {
        name: 'UpdateProduct',
        props: ['id'],

        data() {
            return {
                name: null,
                description: null,
                currentPhoto: null,
                photo: null,
                amount: null,
            }
        },
        created() {
            AdminApi.getProductDetail({id: this.id})
                .then(response => {
                    const data = response.data;
                    this.name = data.name;
                    this.description = data.description;
                    this.currentPhoto = data.photo;
                    this.amount = data.amount.amount;
                })
        },
        methods: {
            updateProduct() {
                let formData = new FormData();
                if (this.photo) {
                    formData.append('photo', this.photo);
                }
                if (this.amount) {
                    formData.append('amount', this.amount)
                }
                formData.append('name', this.name);
                formData.append('description', this.description);
                AdminApi.updateProduct({id: this.id, fields: formData})
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
