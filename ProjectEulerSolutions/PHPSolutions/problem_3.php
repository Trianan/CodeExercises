<?php
  $title = "#3: Largest prime factor";
  $author = "Trianan";
  $question = "The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?";
  $plan = "Since the question number is so large, a good approach would be to divide the number by each prime factor encountered, store the divisor and quotient in a list, and set the new search ceiling to the quotient; inserting into the middle of the list, each pair of divisors and quotients until a divisor equals a quotient. We can then pick the last element as the largest prime factor.";
  $verified_answer = 6857;

  function get_factors($n) {
    $ceiling = $n;
    $divisors = [];
    $quotients = [];
    for ($d = 2; $d < $ceiling; $d++) {
      if ($n % $d == 0) {
        $q = $n / $d;
        $divisors[] = $d;
        $quotients[] = $q;
        $ceiling = $q;
      }
    }
    return array_merge($divisors, array_reverse($quotients));
  }

  function is_prime($n) {
    if ($n == 2) { return true; }
    for ($d = 2; $d < $n; $d++) {
      if ($n % $d == 0) {
        return false;
      }
    }
    return true;
  }
?>

<!DOCTYPE html>
<html>

  <head>
    <title><?= $title ?></title>
    <link href="./resources/styles/style.css" type="text/css" rel="stylesheet">
  </head>

  <body>
    <header>
      <h1>Project Euler: PHP-Edition</h1>
      <h2><?= $title ?><br>By: <?= $author ?></h1>
      <nav><a href="./index.php">Home</a></nav>
    </header>

    <div id="output">
      <p>
        PROGRAM OUTPUT:
      </p>
      <code>
        <?php
          $factors = get_factors(600851475143);
          $max_factor = 1;
          foreach ($factors as $factor) {
            if (is_prime($factor)) {
              if ($factor > $max_factor) {
                $max_factor = $factor;
              }
              echo 'PRIME: ' . $factor . '<br>';
            }
            else {
              echo $factor . '<br>';
            }
          }
        ?>
      </code>
      <p>
        CALCULATED ANSWER:
        <?= $max_factor ?>
      </p>
    </div>

    <div id="problem-sheet">
      <div id="question">
        <h2>Question:</h2>
        <p>
          <?= $question ?>
        </p>
      </div>

      <div id="plan">
        <h2>Plan:</h2>
        <p>
          <?= $plan ?>
        </p>
      </div>
      
      <div id="answer">
        <h2>Answer:</h2>
        <p>Verified: <?= $verified_answer ?></p>
        <p>Calculated: <?= $max_factor ?>
        <?php
          if ($max_factor == $verified_answer) {
            echo "<p class='green'>✓</p>";
          }
          else {
            echo "<p class='red'>✕</p>";
          }
        ?>
      </div>
    </div>

    <footer>
      <div id="footer-links">
        <div>
          <a href="./problem_2.php">&lt-- PREVIOUS</a>
          <a href="./problem_4.php">NEXT --&gt</a>
        </div>
        <a href="./index.php">* HOME *</a>
      </div>
    </footer>
  </body>

</html>