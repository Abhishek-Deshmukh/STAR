<template>
  <div class="row mb-5">
    <div class="col-sm-12 col-md-3">
      <label :for="param"
        >{{ param }} ({{ $store.state.fields[param] }}):</label
      >
    </div>
    <div class="col-sm-12 col-md-9 col-lg-7">
      <!-- integer -->
      <b-form-input
        v-if="$store.state.fields[param] == 'int'"
        v-model="$store.state.values[param]"
        type="number"
        :id="param"
      ></b-form-input>
      <!-- float -->
      <b-form-input
        v-else-if="$store.state.fields[param] == 'float'"
        v-model="$store.state.values[param]"
        type="number"
        :id="param"
        step="any"
      ></b-form-input>
      <!-- string -->
      <b-form-input
        v-else-if="$store.state.fields[param] == 'str'"
        v-model="$store.state.values[param]"
        type="text"
        :id="param"
      ></b-form-input>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
@Component({
  props: { param: String }
})
export default class InputField extends Vue {}
</script>

<style scoped lang="scss">
label {
  font-size: 17px;
  line-height: 35px;
  letter-spacing: 0.046em;
  font-weight: 500;
  font-style: normal;
}
</style>
