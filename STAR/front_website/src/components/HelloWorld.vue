<template>
  <div>
    <div v-for="param in Object.keys($store.state.fields)" :key="param">
      <InputField :param="param" />
    </div>
    <b-button variant="info">Run Task</b-button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import InputField from "./InputField.vue";

@Component({
  components: { InputField }
})
export default class HelloWorld extends Vue {}
</script>
