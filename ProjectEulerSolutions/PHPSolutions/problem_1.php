<?php
  $title = "#1: Multiples of 3 or 5";
  $author = "Trianan";
  $question = "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.";
  $plan = "To ensure that multiples of 3 and 5 aren't double counted, the program will first check each number for being a multiple of 15, then if that is false, check for it being a multiple of 3 or 5.";
  $verified_answer = 233168;

  function sum_multiples($factor_a, $factor_b, $maximum) {
    $sum = 0;
    for ($i = 1; $i < $maximum; $i++) {
      if ($i % ($factor_a * $factor_b) == 0) {
        echo $i . '<br>';
        $sum += $i;
      }
      elseif ($i % $factor_a == 0 || $i % $factor_b == 0) {
        echo $i . '<br>';
        $sum += $i;
      }
    }
    return $sum;
  }
?>

<!DOCTYPE html>
<html>

  <head>
    <title>Project Euler: PHP-Edition -> <?= $title ?></title>
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
          $sum = sum_multiples(3, 5, 1000);;
        ?>
      </code>
      <p>
        CALCULATED ANSWER:
        <?= $sum ?>
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
        <p>Calculated: <?= $sum ?></p>
        <?php
          if ($sum == $verified_answer) {
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
          <a href="./problem_2.php">NEXT --&gt</a>
        </div>
        <a href="./index.php">* HOME *</a>
      </div>
    </footer>
  </body>

</html>