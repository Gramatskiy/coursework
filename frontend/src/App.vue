import json
json.loads(request.body.decode('utf-8'))
<template>
  <div class="container">
    <form @submit.prevent="postProducts">

      <div class="well">
        <h4> Add product</h4>
        <div class="form-group">
          <label class="pull-left"> name </label>
          <input type="text" class="form-control" placeholder="name" v-model="product.name">
        </div>
        <div class="form-group">
          <label class="pull-left"> price </label>
          <input type="text" class="form-control" placeholder="price" v-model="product.price">
        </div>
      </div>

      <button>Post</button>
    </form>
    <div>
      <ul>
        <li v-for="product in products">
          {{product.id + product.name}}
        </li>
      </ul>
      <button @click="getProducts">Get products</button>
    </div>
  </div>
</template>


<script>
  import axios from 'axios';

  export default {
    name: 'hello',
    data() {
      return {
        products: [],
        msg: 'Welcome to Your Vue.js App',
        product: {name: '', price: ''},
      }
    },
    created() {
      this.getProducts();
    },
    methods: {
      postProducts() {
        const newProduct = {
          name: this.product.name,
          price: this.product.price
        };

        console.log(newProduct);
        axios.post("http://localhost:8000/myapp/product/", newProduct)
          .then(() => this.getProducts())
          .catch(reason => console.error(reason.response.data))
      },
      getProducts() {
        axios.get("http://localhost:8000/myapp/product/").then(res => this.products = res.data)
      },
      getOrganizations() {
        axios.get("http://localhost:8000/myapp/organization/").then(res => this.products = res.data)
      }
    }
  }

</script>

<style scoped>
  h1,
  h2 {
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
