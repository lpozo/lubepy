# Luepy

Lubepy is a library that provides a set of basic calculations that applies to machinery lubrication. It's thought to be used by machinery lubrication technicians and engineers to quickly solve urgent lubrication problems on field.

[TOC]

## Installation

```sh
$ pip install lubepy
```

## Usage Example

Say you need to find the viscosity index of an oil. You have viscosity at 40ºC degrees of 104.7 cSt and a viscosity at 100ºC degrees of 13.9 cSt. You can do something like this:

```python
>>> from lubepy.viscosity import viscosity_index
>>> viscosity_index(104.7, 13.9)
134
```

The viscosity index of an oil gives you an idea of how fast the viscosity diminish when the temperature increases.

Now, suppose you have an oil with a viscosity index of 130 and a viscosity at 40ºC degrees of 112 cSt. You need to know what will be the viscosity of your oil at 100ºC degrees. To solve this problem you can do something like this:

```python
>>> from lubepy.viscosity import viscosity_at_100
>>> viscosity_at_100(112, 130)
14.38
```

Most engines work at 100ºC degrees, so it's important to know what will be the viscosity of an engine oil at 100ºC degrees to have an idea of how well this oil will protect your equipments.

## Author

- Leodanis Pozo Ramos – Twitter: [@lpozo78](https://twitter.com/lpozo78) – E-mail: lpozor78@gmail.com

## Technical Contributors

- Alexis Vega Jimenez: Provided formulas and theoretical support.

## Contribute to the Code

1. Make a fork (<https://github.com/lpozo/lubepy/fork>)
2. Clone your fork locally (`git clone https://github.com/your_user_name/lubepy.git`)
3. Create your feature branch (`git checkout -b feature_awesome_feature`)
4. Commit your changes (`git commit -am "Add some awesome feature"`)
5. Push to the branch (`git push -u origin feature_awesome_feature`)
6. Create a new Pull Request against the `develop` branch
7. Wait for code review and feedback

## License

Lubepy is distributed under the GNU GENERAL PUBLIC LICENSE v2. See [LICENSE](https://github.com/lpozo/lubepy) for more information.
