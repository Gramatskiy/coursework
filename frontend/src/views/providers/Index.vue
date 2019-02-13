<template>
    <v-app>
        <v-navigation-drawer
                persistent
                :clipped="clipped"
                v-model="drawer"
                enable-resize-watcher
                fixed
                app
        >
            <v-list>
                <div v-for="(item, i) in items" :key="i">
                    <v-list-tile
                            value="true"
                            class="v-card--hover"
                            @click="item.action"
                            color="success"
                    >
                        <v-list-tile-action class="black--text">
                            <v-icon v-html="item.icon"></v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content class="black--text">
                            <v-list-tile-title v-text="item.title"></v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                    <v-divider></v-divider>
                </div>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar
                app
                :clipped-left="clipped"
        >
            <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
            <v-toolbar-title v-text="title"></v-toolbar-title>
            <v-toolbar-title v-text="lang" @click="changeLang()"></v-toolbar-title>

        </v-toolbar>
        <v-content>
            <router-view></router-view>
        </v-content>
    </v-app>
</template>

<script>
    const [EN, UA] = ['en', 'ua']
    export default {
        name: 'Client',
        data() {
            return {
                clipped: true,
                drawer: false,
                fixed: true,
                items: [
                    {
                        icon: 'receipt',
                        title: "Create received receipt",
                        originTitle: "Create received receipt",
                        action: this.createReceiptReceive
                    },
                    {
                        icon: 'logout',
                        title: 'Logout',
                        originTitle: 'Logout',
                        action: this.logout
                    }
                ],
                right: true,
                rightDrawer: false,
                title: 'MagnitHouse client',
                originTitle: 'MagnitHouse client',
                lang: UA
            }
        },
        created() {
            this.$nextTick(() => {
                for (let item of this.items) {
                    item.title = this.$translate.text(item.originTitle)
                }
                this.title = this.$translate.text(this.originTitle)
            })
        },
        updated() {
            this.$nextTick(() => {
                for (let item of this.items) {
                    item.title = this.$translate.text(item.originTitle)
                }
                this.title = this.$translate.text(this.originTitle)
            })
        },
        methods: {
            logout() {
                this.removeIsPremium();
                this.removeIsProvider();
                this.removeJSONWebToken();
                this.$router.push({name: 'sign-in'})
            },
            createReceiptReceive() {
                this.$router.push({name: 'provider-receipt-receive-create'})
            },
            changeLang() {
                if (this.lang === UA) {
                    this.$translate.setLang(EN);
                    this.lang = EN
                } else {
                    this.$translate.setLang(UA);
                    this.lang = UA
                }
            }
        }
    }
</script>

<style scoped>

</style>
