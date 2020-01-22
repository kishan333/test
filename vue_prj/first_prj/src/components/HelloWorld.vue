<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <button @click="getQuestion"> Get ques_id</button>
    <p>{{ ques_id }}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data: function() {
    return {
    ques_id : null,
    
  }
  },
  methods: {
      getQuestion: function() {
        
          let api_url = 'http://localhost:8000/pollstest/detail/'; 
          this.$http.get(api_url).then((response) => {
                console.log(response.content)
                //this.articles = response.data;

              })
              .catch((err) => {
              console.log(err);
              })
              }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
h3 {
  margin: 40px 0 0;
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
