import styles from './styles.module.scss'

export function StandartButton(props) {
	const link = props.link ? props.link : '/'
	return (
		<a className={styles.button} href={link}>
			{props.children}
		</a>
	)
}
