<template>
  <div class="row mb-5">
    <div class="col-sm-12 col-md-3">
      <label :for="field.name">{{ field.name }}({{ field.type }}):</label>
    </div>
    <div class="col-sm-12 col-md-9 col-lg-7">
      <!-- integer -->
      <b-form-input
        v-if="field.type == 'int'"
        v-model="$store.state.values[field.id]"
        type="number"
        :id="field.name"
      ></b-form-input>
      <!-- float -->
      <b-form-input
        v-else-if="field.type == 'float'"
        v-model="$store.state.values[field.id]"
        type="number"
        :id="field.name"
        step="any"
      ></b-form-input>
      <!-- string -->
      <b-form-input
        v-else-if="field.type == 'str'"
        v-model="$store.state.values[field.id]"
        type="text"
        :id="field.name"
      ></b-form-input>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
@Component({
  props: { field: Object }
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
