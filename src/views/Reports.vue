<script lang="ts" setup>
import Button from "primevue/button";
import "primeicons/primeicons.css";
import Fliter from "../components/reportspage/Filter.vue";
import Sidebar from "../components/Sidebar.vue";
import Results from "../components/reportspage/Result.vue";
import Title from "../components/reportspage/Title.vue";
import ImageParagraph from "../components/reportspage/ImageParagraph.vue";
import Paragraph from "../components/reportspage/Paragraph.vue";
import { ref, reactive, watch } from "vue";
import axios from "axios";
import dailyQuestionnaire from "../modules/questions.ts";
import RadioButton from "primevue/radiobutton";
import { UserType } from "@/modules/Basic";
import Dialog from "primevue/dialog";
import { HttpRequester } from '@/services/ApiCaller.ts';

const userId = UserType.getInstance().getUserId()
const showDialog = ref(false);
const message = ref("");

const plants = ref([]);
const days = ref();
const locations = ref();
let a = new Array(dailyQuestionnaire.questions.length).fill(null);
const selectedAnswer = ref<any[]>(a);

async function get_images() {
  const requester = new HttpRequester('get_summary');
  const requester_data = await requester.callApi('GET');
  plants.value = requester_data.summary_data
  console.log("plants.value", plants.value)

  // await axios.post('http://127.0.0.1:8000/get_summary',{},{}).then((res:any)=>{plants.value = res.data.data})
  days.value =  [...new Set(plants.value.map((obj:any) => obj.Date))];
  locations.value =  [...new Set(plants.value.map((obj:any) => obj.Location))];
}
get_images();

const selectedDay = ref();
const selectedLocation = ref();
const status = ref();
const allComponents = [Title, ImageParagraph, Paragraph];

const components = reactive([
  {
    id: "0",
    order: 0,
    title: "The Report Title",
    imagePath: "",
    paragraph: "type the paragraph here",
    info: {},
  },
]);

function addImageParagraphComponent(id: string, path: string) {
  components.push({
    id: id,
    order: 1,
    title: "The Paragraph Title",
    imagePath: path,
    paragraph: "Type the paragraph here",
    info: {},
  });
}
let lastOrder = 0;
function addParagraphComponent() {
  lastOrder = lastOrder + 1;
  components.push({
    id: lastOrder.toString(),
    order: 2,
    title: "The Paragraph Title",
    imagePath: "",
    paragraph: "Type the paragraph here",
    info: {},
  });
}
function save() {
  console.log(1);
  const hasNull = selectedAnswer.value.some((element) => element === null);
  if (hasNull) {
    console.log(2);
    showDialog.value = true;
    message.value = "Please Answer Questions First";
  } else {
    let date = new Date();

    const report = {
      expert_id: userId,
      created_at: date.toDateString(),
      components: [] as any[],
      questions_answers: [] as any[],
    };

    for (let com of components) {
      report.components.push({
        id: com.id,
        order: com.order,
        title: com.title,
        imagePath: com.imagePath || "",
        paragraph: com.paragraph,
      });
    }
    for (let i = 0; i < selectedAnswer.value.length; i++) {
      if (selectedAnswer.value[i]) {
        report.questions_answers.push({
          question_order: i,
          question_answer: selectedAnswer.value[i],
        });
      }
    }

    axios.post("http://127.0.0.1:8000/api/v1/add_report", report, {}).then((res) => {
      console.log(res);
      message.value = "Added Succesfully";
      showDialog.value = true;
    });
  }
}
</script>

<template>
  <div class="report-container">
    <Dialog
    style=' width:50rem'
      v-model:visible="showDialog"
      modal
      :pt="{
        root: 'border-none',
        mask: {
          style: 'backdrop-filter: blur(2px)',
        },
      }"
    >
      <div
        style="
          display: flex;
          flex-direction: column;
          gap: 2rem;
          align-items: center;
          justify-content: center;
        "
      >
        <h1>{{ message }}</h1>
        <Button label="Cancel" @click="showDialog=false"/>
      </div>
    </Dialog>
    <Sidebar class="sidebar" :selected="3" />
    <div class="summary-container">
      <div class="main-container">
        <Fliter
          :days="days"
          :locations="locations"
          @day="
            (v) => {
              v ? (selectedDay = v) : (selectedDay = v);
            }
          "
          @location="
            (v) => {
              v ? (selectedLocation = v) : (selectedLocation = v);
            }
          "
          @status="
            (v) => {
              v ? (status = v) : (status = v);
            }
          "
          class="filter"
        />
        <Results
          :plants="plants"
          :day="selectedDay"
          :location="selectedLocation"
          :status="status"
          class="results"
          @data="
            (e) => {
              addImageParagraphComponent(e.id, e.path);
            }
          "
        />
      </div>
    </div>

    <div class="questions">
      <div class="questions-wrapper">
        <h3>Please Fill The Following Questions</h3>

        <div
          class="question"
          v-for="(question, i) in dailyQuestionnaire.questions"
          :key="question.key"
        >
          <h4>{{ question.question }}</h4>
          <div
            v-for="option in question.options"
            :key="option.key"
            class="flex align-items-center"
          >
            <RadioButton
              v-model="selectedAnswer[i]"
              :inputId="option.key"
              name="dynamic"
              :value="option.text"
            />
            <label style="margin-left: 0.5rem" :for="option.key" class="ml-2">{{
              option.text
            }}</label>
          </div>
        </div>
      </div>
    </div>

    <div class="page-area">
      <div class="report-components-wraper">
        <component
          v-for="(component, i) in components"
          :key="component.id"
          :is="allComponents[component.order]"
          :paragraph="component.paragraph"
          :imageid="component.imagePath"
          :title="component.title"
          @delete="components.splice(i, 1)"
          @titleChange="
            (e) => {
              typeof e === 'string' ? (components[i].title = e) : undefined;
            }
          "
        />
      </div>
      <div class="action-container">
        <Button label="Save" @click="save" />
        <i
          class="pi pi-plus-circle"
          @click="
            () => {
              addParagraphComponent();
            }
          "
          style="
            color: var(--accentb);
            font-size: 32px;
            display: block;
            cursor: pointer;
          "
        ></i>
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
  grid-template-columns: 100px 250px 1fr 2fr;
}
.summary-container {
  background-color: var(--primary);
  position: relative;
}
.main-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  gap: 16px;
}
.sidebar {
  position: sticky;
  top: 0;
}
.page-area {
  background-color: var(--primary);
}

.questions {
  background-color: var(--primary);
}
.report-components-wraper {
  width: 90%;
  margin-inline: auto;
  background-color: white;
  min-height: 80vh;
  margin-top: 32px;
  border-radius: 8px;
  padding: 64px;
}
h3 {
  text-align: center;
  color: var(--accentb);
  font-weight: bolder;
}
.question {
  box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
    rgba(60, 64, 67, 0.15) 0px 2px 6px 2px;
  margin-top: 1rem;
  padding: 0.5rem;
  border-radius: 4px;
}
.questions-wrapper {
  width: 95%;
  margin-inline: auto;
  background-color: white;
  height: 80vh;
  margin-top: 32px;
  border-radius: 8px;
  padding: 2rem 1rem;
  overflow-y: scroll;
}

button {
  width: 20%;
  font-size: 24px;
  border-radius: 8px;
  height: 48px;

  background-color: var(--accentb);
}
.action-container {
  width: 90%;
  margin-inline: auto;
  padding: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 32px;

  background-color: white;
}
</style>
