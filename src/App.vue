<script setup>
  import {RouterView} from "vue-router"
</script>
<template>
  <RouterView />
</template>

<style>
body{
  padding: 0;
  margin: 0;
}
body,#app{
  font-family: Georgia, 'Times New Roman', Times, serif;
  min-width: 100vw;
  min-height: 100vh;
}
:root{
  --primary:#d8d8d8;
  --secondary:#28a745;
  --accenta:#1f271a;
  --accentb:#ef9107;
}
</style>