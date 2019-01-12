<template>
  <div id="app">
    <ul>
      <li v-for="product in products">
        {{product.id+product.name}}
      </li>
    </ul>
    <button @click='getProducts'>Get products</button>
    <button @click='getOrganizations'>Get organization</button>
     <li v-for="organization in organizations">
        {{organization.id+organization.name}}
     </li>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: 'app',
  data: function() {
    return {
      products: [],
      msg: 'Welcome'
    }
  },
  methods: {
    getProducts() {
      axios.get("http://localhost:8000/myapp/product").then(res => this.products = res.data);
    },
    getOrganizations() {
      axios.get("http://localhost:8000/myapp/organization").then(res => this.products = res.data);
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
