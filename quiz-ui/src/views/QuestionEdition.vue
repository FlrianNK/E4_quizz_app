<template>
  <div class="QuestionEdition">
    <h1>QuestionEdition</h1>
    - un champ d’édition “Position” permettant de modifier la position de la
    question dans le quiz - un champ d’édition “Titre” - un champ d’édition
    “Intitulé” - un bouton d’upload d’image + aperçu de l’image chargée - une
    liste de quatre éditions de réponses possibles, avec chacune : - un champ
    d’édition “Intitulé de la réponse” - une “checkbox” spécifiant la réponse
    correcte parmi les quatre - un bouton de sauvegarde (retour à la liste avec
    sauvegarde) - un bouton d’annulation (retour à la liste sans sauvegarde)
  </div>
</template>

<script>
export default {
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
};
</script>
