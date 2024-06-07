<script setup lang="ts">
import axios from "axios";
import { ref } from "vue";
import Sidebar from "@/components/Sidebar.vue";
import Title from "../components/ownerReport/Title.vue";
import ImageParagraph from "../components/ownerReport/ImageParagraph.vue";
import Paragraph from "../components/ownerReport/Paragraph.vue";
import dailyQuestionnaire from "@/modules/questions";

const reports = ref();
axios.get("http://rowling-backend3.eastus.azurecontainer.io:8000/api/v1/get_all_reports", {}).then((res) => {
  console.log("res", res)
  reports.value = res.data.data;
});
const selectedReport=ref(0)

const allComponents = [Title, ImageParagraph, Paragraph];
</script>

<template>
 

  <div class="report-container">
    <Sidebar class="sidebar" :selected="3" />
    <div class="summary-container">
      <div class="main-container">
        <div class="card" :class="{selected:(selectedReport==i)}" v-for="report,i in reports" @click="selectedReport=i">
        <p><strong>Date: </strong> {{ report.created_at }}</p>
            <p>
              <strong>Title: </strong> 
        {{ report.components[0].title }}</p>
        <p><strong>Expert:</strong>  {{report.expert_id}}</p>
        </div>
       
      </div>
    </div>
    <div class="page-container">
        <div v-if="reports" class="report-components-wraper">
            <component
          v-for="(component, i) in reports[selectedReport]?.components"
          :key="component.id"
          :is="allComponents[component.order]"
          :paragraph="component.paragraph"
          :imageid="component.imagePath"
          :title="component.title"
        
        />
        <div class="questions-answers" v-if="reports[selectedReport].questions_answers">
          <div v-for="(question,i) in dailyQuestionnaire.questions" class="question">
            <h4 >{{question.question}}</h4>
            <p>{{ reports[selectedReport]?.questions_answers[i]?.question_answer }}</p>
          </div>
        </div>
        </div>
    </div>
  </div>
</template>

<style scoped>

.report-container {
  width: 100%;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: 100px 300px 1fr;
  background-color: var(--primary);
}
.summary-container {
  position: relative;
}
.sidebar {
  position: sticky;
  top: 0;
}
.main-container {
  display: flex;
  align-items: center;
  flex-direction: column;


}
p{
    margin: 0;
}
.card{
    margin-top: 1rem;
 
background-color: white;
 display: flex;
 flex-direction: column;
 padding: 0.5rem 2rem;  
 cursor: pointer;
 transition-duration: 0.5s;
}
.card:hover{
    scale: 1.1;
}
.report-components-wraper {
  width: 95%;
  background-color: white;
  border-radius: 8px;
  padding: 1rem ;
  margin-top: 1rem;
}
.selected{
    background-color: var(--secondary);
}
.question{
  display: flex;
  flex-direction: column;
  margin: 1rem;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: rgba(0, 0, 0, 0.2) 0px 18px 50px -10px;

}
</style>
