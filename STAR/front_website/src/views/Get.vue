<template>
  <div class="container">
    <OutputComp />
  </div>
</template>

<script>
// @ is an alias to /src
import OutputComp from "@/components/OutputComp.vue";

export default {
  name: "Home",
  components: {
    OutputComp
  }
};
</script>
