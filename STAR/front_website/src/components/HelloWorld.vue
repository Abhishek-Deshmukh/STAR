<template>
  <div>
    <InputField
      v-for="param in Object.keys($store.state.fields)"
      :key="param"
      :param="param"
    />
    <b-button variant="info" @click="sendRunCommand" class="mb-2"
      >Run Task</b-button
    >
    <br />
    <code v-if="$store.state.runButtonClicked" @click="goToGet">{{
      $store.state.runInstanceData
    }}</code>
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
  @Action("fetchParams") fetchParams: void;
  @Action("sendRunCommand") sendRunCommand: void;

  goToGet() {
    this.$router.push("/get");
  }
  created() {
    this.fetchParams();
  }
}
</script>
