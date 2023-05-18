<template>
  <div class="QuestionEdition">
    <h1>QuestionEdition</h1>
    <h2>Position</h2>
    <input type="text" v-model="position" />
    <h2>Titre</h2>
    <input type="text" v-model="title" />
    <h2>Intitulé</h2>
    <input v-model="text" />
    <h2>Image</h2>
    <ImageUpload @file-change="imageFileChangedHandler" />
    <p>Aperçu</p>
    <img :src="image" alt="Base64 Image" />
    <h2>Choix des réponses</h2>
    <div>
      <input type="text" v-model="possibleAnswersText[0]" />
      <input type="radio" v-model="rightAnswer" value="0" />
    </div>
    <div>
      <input type="text" v-model="possibleAnswersText[1]" />
      <input type="radio" v-model="rightAnswer" value="1" />
    </div>
    <div>
      <input type="text" v-model="possibleAnswersText[2]" />
      <input type="radio" v-model="rightAnswer" value="2" />
    </div>
    <div>
      <input type="text" v-model="possibleAnswersText[3]" />
      <input type="radio" v-model="rightAnswer" value="3" />
    </div>
    <button type="button" @click="save">Sauvegarder</button>
    <button type="button" @click="cancel">Annuler</button>
  </div>
</template>

<script>
import ImageUpload from "./ImageUpload.vue";
export default {
  props: {
    question: {
      type: Object,
      required: true,
    },
    edit: {
      type: Boolean,
      required: true,
    },
  },
  components: {
    ImageUpload,
  },
  data() {
    return {
      position: this.question.position,
      title: this.question.title,
      text: this.question.text,
      image: this.question.image,
      possibleAnswersText: ["", "", "", ""],
      rightAnswer: 0,
    };
  },
  created() {
    for (let i = 0; i < this.question.possibleAnswers.length; i++) {
      this.possibleAnswersText[i] = this.question.possibleAnswers[i].text;
    }
    this.rightAnswer = this.question.possibleAnswers.findIndex(
      (answer) => answer.isCorrect == true
    );
  },
  methods: {
    imageFileChangedHandler(b64String) {
      if (b64String) {
        this.image = b64String;
      } else {
        this.image = this.question.image;
      }
    },
    save() {
      if (this.edit) {
        console.log("edit");
      } else {
        console.log("add");
      }
    },
    cancel() {
      this.$router.push("/admin");
    },
  },
};
</script>
