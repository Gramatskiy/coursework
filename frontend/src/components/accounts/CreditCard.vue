<template>
  <v-flex row class="justify-center d-flex column">
    <form ref="form" class="card-form" @submit.prevent="$emit('submit')">
      <header>
        <h2 >{{t("Your card data")}}</h2>
      </header>
      <div class="card-form-field">
        <label for="cardNumberInput" class="card-form-field__label" >{{t("Number")}}</label>
        <input type="text"
               name="card[number]"
               v-model="card.number"
               maxlength="16"
               class="card-form-field__input"
               ref="card.number"
               required
               id="cardNumberInput"/>
      </div>
      <div class="card-form-field">
        <label for="cardOwnerInput" class="card-form-field__label" >{{t("Owner name")}}</label>
        <input type="text"
               required
               name="card[owner]"
               v-model="card.owner"
               class="card-form-field__input"
               maxlength="24"
               ref="card.owner"
               id="cardOwnerInput"/>
      </div>
      <div class="card-form-field">
        <label  class="card-form-field__label card-form-field__label_inline" >{{t("Expiration")}}</label>
        <select v-model="card.expiration.month"
                name="card[expiration][month]"
                class="card-form-field__select"
                required
                ref="card.expiration.month">
          <option v-for="month in months" :key="month">{{month}}</option>
        </select>
        /
        <select v-model="card.expiration.year"
                name="card[expiration][year]"
                class="card-form-field__select"
                required
                ref="card.expiration.year">
          <option v-for="year in years" :key="year">{{year}}</option>
        </select>
      </div>
      <div class="card-form-field">
        <label for="cardCvcInput" class="card-form-field__label card-form-field__label_inline">CVC</label>
        <input type="text"
               name="card[cvc]"
               v-model="card.cvc"
               maxlength="3"
               required
               class="card-form-field__input card-form-field__input_cvc"
               id="cardCvcInput"
               ref="card.cvc"/>
      </div>
      <v-btn type="submit" class="success" >{{t("Checkout")}}</v-btn>
    </form>

    <div class="card-preview">
      <div class="card-preview__side card-preview__side_front">
        <div class="card-preview__number">
          <div class="card-preview__label card-preview__label_white" >{{t("Number")}}</div>
          <div class="card-preview__etched-text">{{cardNumberFormatted}}</div>
        </div>

        <div class="card-preview__owner">
          <span class="card-preview__label card-preview__label_white" >{{t("Owner")}}</span>
          <span class="card-preview__etched-text">{{card.owner}}</span>
        </div>

        <div class="card-preview__expiration">
          <span class="card-preview__label card-preview__label_white" >{{t("Valid through")}}</span>
          <span class="card-preview__etched-text">{{cardExpiration}}</span>
        </div>
      </div>
      <div class="card-preview__side card-preview__side_back">
        <div class="card-preview__cvc">
          <span class="card-preview__label" >{{t("CVC")}}</span>
          {{card.cvc}}
        </div>
      </div>
    </div>
  </v-flex>
</template>

<script>

export default {
  name: 'Card',
  props: ['value'],
  data () {
    return {
      card: {
        number: '',
        owner: '',
        expiration: {
          month: '',
          year: ''
        },
        cvc: ''
      }
    }
  },

  computed: {
    cardNumberFormatted: function () {
      var numberChunks = this.card.number.match(/.{1,4}/g)

      if (numberChunks) {
        return numberChunks.join(' ')
      } else {
        return ''
      }
    },
    cardExpiration: function () {
      if (!this.card.expiration.month || !this.card.expiration.year) {
        return ''
      }

      return this.card.expiration.month + '/' + this.card.expiration.year
    },
    months: function () {
      return [
        '01', '02', '03', '04',
        '05', '06', '07', '08',
        '09', '10', '11', '12'
      ]
    },
    years: function () {
      let years = []
      const currentYear = (new Date()).getFullYear() % 2000

      for (var i = 0; i < 18; i++) {
        years.push(currentYear + i)
      }

      return years
    }
  },
  watch: {
    'card.number':

      function (newNumber) {
        this.card.number = newNumber.replace(/[^0-9]/gim, '')
      },
    'card.owner':

      function (newOwner) {
        this.card.owner = newOwner.toUpperCase().replace(/[^A-Z\s]/gim, '')
      },
    'card.cvc':
      function (newCvc) {
        this.card.cvc = newCvc.replace(/[^0-9]/gim, '')
      }
  }
}
</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css?family=Montserrat');

  $bp-sm: 768px;
  $bp-md: 1024px;

  $black: #000;
  $orange: #FF6D00;
  $gray: #999;
  $white: #fff;

  $main-font: 'Montserrat', sans-serif;

  $transition-speed: .3s;

  .card-form {
    box-sizing: border-box;
    padding: 16px;
    width: 100%;
    max-width: 400px;
    margin-left: 100px;
    background-color: $white;
    box-shadow: 4px 4px 16px rgba($black, .8);

    @media (min-width: $bp-sm) {
      margin-top: 64px;

    }
    @media (min-width: $bp-md) {
      display: inline-block;
      margin: 64px 0 0;
      margin-left: 400px;
    }

    &__title {
      text-align: center;
      color: $orange;

    }
    &__submit {
      padding: 8px 16px;
      border: 1px solid $orange;
      font-size: 18px;
      text-transform: uppercase;
      font-weight: bold;
      border-radius: 2px;
      color: $white;
      background-color: $orange;
      transition: color $transition-speed,
      background $transition-speed,
      box-shadow $transition-speed;

      &:hover,
      &:focus {
        outline: none;
        color: $orange;
        background-color: $white;
        box-shadow: 0 0 8px $orange;

      }
    }
  }

  .card-form-field {
    margin: 8px 0 16px;

    &__label {
      display: block;
      margin-bottom: 4px;

      &_inline {
        display: inline-block;
        margin-bottom: 0;
        margin-right: 4px;

      }

    }
    &__input {
      box-sizing: border-box;
      width: 100%;
      padding: 4px 8px;
      font-size: 18px;
      font-family: $main-font;
      border-radius: 2px;
      border: 1px solid $gray;
      transition: box-shadow $transition-speed;

      &:focus {
        outline: none;
        box-shadow: 0 0 8px $orange;

      }

      &_cvc {
        width: 54px;

      }
    }
    &__select {
      box-sizing: border-box;
      padding: 4px 8px;
      font-size: 18px;
      font-family: $main-font;
      background-color: $white;
      border-radius: 2px;
      border: 1px solid $gray;
      transition: box-shadow $transition-speed;

      &:focus {
        outline: none;
        box-shadow: 0 0 8px $orange;

      }
    }
  }

  .card-preview {
    position: relative;
    display: none;
    vertical-align: top;
    margin-top: calc(64px + 53px);
    margin-left: 32px;
    margin-right: 10px;
    user-select: none;

    @media (min-width: $bp-md) {
      display: inline-block;

    }

    &__side {
      position: relative;
      width: 400px;
      height: 252px;
      border-radius: 16px;
      background-color: $white;
      box-shadow: 2px 2px 2px rgba($black, .5);

      &_front {
        z-index: 2;
        background-color: #009E8E;
        box-shadow: 2px 2px 6px rgba($black, .6);

      }
      &_back {
        position: absolute;
        z-index: 1;
        top: 32px;
        left: 128px;
        background: lightgray linear-gradient(to bottom, $white 24%, $black 24%, $black 40%, $white 40%);

      }
    }
    &__label {
      font-size: 12px;
      color: $gray;
      text-transform: uppercase;

      &_white {
        color: $white;

      }
    }
    &__cvc {
      position: absolute;
      top: 50%;
      left: 280px;

    }
    &__number {
      position: absolute;
      top: 32%;
      left: 16px;
      font-size: 34px;

    }
    &__owner {
      position: absolute;
      left: 16px;
      bottom: 40px;

    }
    &__expiration {
      position: absolute;
      left: 16px;
      bottom: 16px;

    }
    &__etched-text {
      text-shadow: 1px 1px 4px #000;
      color: #fff;

    }
  }
</style>
