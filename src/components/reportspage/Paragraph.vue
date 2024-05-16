<script lang="ts" setup>
import "primeicons/primeicons.css";
import plants from "@/modules/plants";
import { defineProps, defineEmits, ref } from "vue";

const props = defineProps(["title", "paragraph"]);
const Title = ref(props.title);
const paragraph = ref(props.paragraph);
const emit = defineEmits(["titleChange", "paragraphChange",'delete']);
</script>

<template>
  <div class="paragraph-wraper">
    <i class="pi pi-times-circle" @click="emit('delete')"></i>
    <main>
      <div class="paragraph-container">
        <input
          type="text"
          @change="emit('titleChange', Title)"
          v-model="Title"
        />
        <textarea
          oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"'
          v-model="paragraph"
          @change="emit('paragraphChange', paragraph)"
        ></textarea>
      </div>
    </main>
  </div>
</template>

<style scoped>
.paragraph-wraper{
    display: flex;
    flex-direction: column;
    border-bottom: 2px solid var(--accentb);
}
main {
  margin-block: 4px;
}
.paragraph-container {
  display: flex;
  flex-direction: column;
}
textarea {
  resize: none;
}
input {
  font-weight: bold;
  color: var(--secondary)
}
input,
textarea {
  border: 0px;
}
textarea {
  padding-left: 8px;
}
i {
    margin-right: 24px;
  align-self: flex-end;
  cursor: pointer;
  color: var(--accenta);
  margin-top: 8px;
}
</style>
