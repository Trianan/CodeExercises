<?php
  $title = "#2: Even Fibonacci numbers";
  $author = "Trianan";
  $question = "Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.";
  $plan = "We will generate each term in a loop, but instead of storing in a list, we'll check for even terms as they're calculated, and add them to the sum.";
  $verified_answer = 4613732;

  function get_fibosum($term_0, $term_1, $max_term) {
    $sum = ($term_0 % 2 == 0)? $term_0 : 0;
    echo $term_0 . '<br>';

    while ($term_1 < $max_term) {
      echo $term_1 . '<br>';
      if ($term_1 % 2 == 0) { $sum += $term_1; }
      $swap = $term_0 + $term_1;
      $term_0 = $term_1;
      $term_1 = $swap;
    }
    return $sum;
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
          $sum = get_fibosum(1, 2, 4000000);
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
        <p>Calculated: <?= $sum ?>
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
          <a href="./problem_1.php">&lt-- PREVIOUS</a>
          <a href="./problem_3.php">NEXT --&gt</a>
        </div>
        <a href="./index.php">* HOME *</a>
      </div>
    </footer>
  </body>

</html>