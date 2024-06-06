<script lang="ts" setup>
import "primeicons/primeicons.css";
import { defineProps, defineEmits, ref } from "vue";

const props = defineProps(["title", "imageid", "paragraph"]);
const Title = ref(props.title);
const imageid = ref(props.imageid);
const paragraph = ref(props.paragraph);
const emit = defineEmits(["titleChange", "paragraphChange",'delete']);
function transform(url:string){
  const regex = /\/d\/(.*)\/view/;
  const match = url.match(regex);
  
  if (match) {
    const imageId = match[1];
    url= `https://drive.google.com/uc?id=${imageId}&export=download`;
    
  } 


  url=url.replace("&export=download", "");
  url=url.replace("google", "lienuc");
  return url
}
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
      <img :src="transform(imageid)" alt=""  crossorigin="anonymous" />
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
  display: grid;
  grid-template-columns: 2fr 1fr;
  margin-block: 4px;
}
.paragraph-container {
  display: flex;
  flex-direction: column;
}
textarea {
  resize: none;
}
img {
  width: 90%;
  aspect-ratio: 1/0.8;
  display: inline-block;
  margin-inline: auto;
  border-radius: 8px;
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
