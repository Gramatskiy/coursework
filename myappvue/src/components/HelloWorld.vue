<template>
  <div class="hello">

  </div>
</template>

<script>
import axios from 'axios'
export default {
name: 'HelloWorld',
  data () {
    return {
      users: [] // Array for holding the tasks
    }
  },
  mounted () { // This will be called when HelloWorld is loaded
    this.getUsers(); // Call our getTasks function below
  },
  methods: {
    getUsers() {
        axios({
            method:'get',
            url: 'http://http://127.0.0.1:8000/account/users//',
            auth: {
                username: 'admin',
                password: 'admin'
            }
        }).then(response => this.users = response.data);
    }
  }
}
</script>

<style scoped>
.select, select { /* 100% width for the select */
  width: 100%;
}

.card { /* Adding some air under the tasks */
  margin-bottom: 25px;
}

.done { /* Make the done tasks a little bit transparent */
  opacity: 0.3;
}
</style>
