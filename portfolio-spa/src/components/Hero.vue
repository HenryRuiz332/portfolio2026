<template>
  <section id="home-section" class="hero" style="background: #000; overflow: hidden; height: 100vh; min-height: 700px; position: relative;">
    <div class="home-slider" style="position: relative; height: 100%; width: 100%;">
      <transition name="fade">
        <div :key="currentSlide" class="slider-item" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0;">
          
          <div class="container-fluid p-0" style="height: 100%;">
            <div class="row no-gutters slider-text align-items-center justify-content-end" style="height: 100%; position: relative; margin: 0;">
              
              <!-- Image Section (Right) -->
              <div class="one-third order-md-last img" 
                   :style="{ 
                     backgroundImage: `url(${slides[currentSlide].image})`, 
                     height: '100%', 
                     width: '60%', 
                     backgroundSize: 'cover', 
                     backgroundPosition: 'center',
                     position: 'relative'
                   }">
                <div class="overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.1);"></div>
              </div>

              <!-- Text Section (Left - Absolute Positioning to overlap) -->
              <div class="one-forth d-flex align-items-center" 
                   style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; z-index: 10; pointer-events: none;">
                <div class="container" style="pointer-events: auto;">
                  <div class="row">
                    <div class="col-md-7 col-lg-6">
                      <div class="text" data-aos="fade-up" data-aos-duration="1000">
                        <span class="subheading" style="color: #ffbd39; font-weight: 600; font-size: 14px; letter-spacing: 3px; text-transform: uppercase; display: block; margin-bottom: 20px;">Hello!</span>
                        <h1 class="mb-4 mt-3" style="font-size: 60px; font-weight: 800; line-height: 1.2; color: #fff; margin-bottom: 30px !important;">
                          I'm <span style="color: #ffbd39;">Clark Thompson</span>
                        </h1>
                        <h2 class="mb-4" style="font-size: 30px; font-weight: 400; color: #fff; margin-bottom: 30px !important;">
                          A Freelance Web Designer
                        </h2>
                        <p>
                          <a href="#" class="btn btn-primary py-3 px-4" style="background: #ffbd39; border: 1px solid #ffbd39; color: #000; border-radius: 30px; padding: 12px 30px; text-transform: uppercase; font-weight: 600; font-size: 12px; letter-spacing: 2px;">Hire me</a>
                          <a href="#" class="btn btn-white btn-outline-white py-3 px-4 ml-2" style="background: transparent; border: 1px solid rgba(255,255,255,0.5); color: #fff; border-radius: 30px; padding: 12px 30px; text-transform: uppercase; font-weight: 600; font-size: 12px; letter-spacing: 2px; margin-left: 10px;">My works</a>
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

            </div>
          </div>

        </div>
      </transition>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick, watch } from 'vue';
import bg1 from '@/assets/images/bg_1.png';
import bg2 from '@/assets/images/bg_2.png';
import AOS from 'aos';

const slides = ref([
  {
    image: bg1,
    title: "I'm <span>Clark Thompson</span>",
    description: 'A Freelance Web Designer'
  },
  {
    image: bg2,
    title: "I'm a <span>web designer</span> based in London",
    description: 'Freelance Design'
  }
]);

const currentSlide = ref(0);
let slideInterval = null;

watch(currentSlide, () => {
  nextTick(() => {
    AOS.refresh();
  });
});

onMounted(() => {
  slideInterval = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.value.length;
  }, 5000);
});

onUnmounted(() => {
  if (slideInterval) clearInterval(slideInterval);
});
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 1.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.text span {
  color: #ffbd39;
}
</style>