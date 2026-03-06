<template>
  <section class="ftco-section ftco-no-pt ftco-no-pb ftco-counter img" id="section-counter">
    <div class="container">
      <div class="row d-md-flex align-items-center">
        <div v-for="(item, index) in counters" :key="index" class="col-md d-flex justify-content-center counter-wrap ftco-animate">
          <div class="block-18">
            <div class="text">
              <strong class="number" :data-number="item.number">{{ item.currentValue }}</strong>
              <span>{{ item.label }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const counters = ref([
  { label: 'Awards', number: 100, currentValue: 0 },
  { label: 'Complete Projects', number: 1200, currentValue: 0 },
  { label: 'Happy Customers', number: 1200, currentValue: 0 },
  { label: 'Cups of coffee', number: 500, currentValue: 0 }
]);

onMounted(() => {
  // Simple intersection observer to trigger animation
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounters();
        observer.disconnect();
      }
    });
  }, { threshold: 0.5 });

  const section = document.querySelector('#section-counter');
  if (section) observer.observe(section);
});

const animateCounters = () => {
  counters.value.forEach(counter => {
    let start = 0;
    const end = counter.number;
    const duration = 2000;
    const increment = end / (duration / 16);
    
    const timer = setInterval(() => {
      start += increment;
      if (start >= end) {
        counter.currentValue = end;
        clearInterval(timer);
      } else {
        counter.currentValue = Math.floor(start);
      }
    }, 16);
  });
};
</script>
