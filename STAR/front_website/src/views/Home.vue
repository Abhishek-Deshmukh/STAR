<template>
  <div class="container">
    <HelloWorld />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    HelloWorld
  },
  created() {
    axios.get("http://localhost:5000/params").then(response => {
      this.$store.state.fields = response.data;
      console.log(this.$store.state.fields);
      console.log(response);
    });
  }
};
</script>
