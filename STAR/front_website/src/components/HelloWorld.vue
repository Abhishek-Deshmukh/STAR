<template>
  <div>
    <div v-for="param in Object.keys($store.state.fields)" :key="param">
      <InputField :param="param" />
    </div>
    <b-button variant="info" @click="sendRunCommand">Run Task</b-button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import InputField from "./InputField.vue";
import { Action } from "vuex-class";

@Component({
  components: { InputField }
})
export default class HelloWorld extends Vue {
  @Action("fetchParams") fetchParams;
  @Action("sendRunCommand") sendRunCommand;
  created() {
    this.fetchParams();
  }
}
</script>
