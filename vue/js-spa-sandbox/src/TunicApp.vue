<script setup>
import HorizontalPanels from '@/components/HorizontalPanels.vue'
import VerticalPanels from '@/components/VerticalPanels.vue'
</script>

<template>
  <HorizontalPanels left-initial-width="40%">
    <template #left>
      <VerticalPanels topInitialHeight="60%">
        <template #top>
          Rune Keyboard
        </template>
        <template #bottom>
          Rune Editor
        </template>
      </VerticalPanels>
    </template>
    <template #right>
      Rune Document
    </template>
  </HorizontalPanels>
</template>

<style scoped></style>
