<script setup>
import { RouterView } from "vue-router";
</script>
<template>
  <RouterView />
</template>

<style>
body {
  padding: 0;
  margin: 0;
}
body,
#app {
  font-family: sans-serif;
  min-width: 100vw;
  min-height: 100vh;
  color: var(--accenta);

}

:root {
  --primary: #e5e5e5;
  --secondary: #05a500;
  --accenta: #1f271a;
  --accentb: #dbce03;
  --text: #d8ffd6;
  --card:#fff
}
</style>
