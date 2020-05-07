<template>
  <div>
    <div v-for="field in fields" :key="field.id">
      <InputField v-bind:field="field" />
    </div>
    {{ this.$store.state.values }}
    <br>
    <b-button variant="info">Run Task</b-button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import InputField from "./InputField.vue";

@Component({
  components: {
    InputField
  }
})
export default class HelloWorld extends Vue {
  fields: object[] = [
    { name: "smhint", id: 0 },
    { name: "lmao", id: 1 }
  ];
}
</script>
