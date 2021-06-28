import styles from './styles.module.scss'
import { IoBusiness } from 'react-icons/io5'
import { FaCalendarAlt, FaMapMarkerAlt, FaRegMoneyBillAlt } from 'react-icons/fa'
import Link from 'next/link'

interface CardProps {
	id: number
	title: string
	company: string
	field: string
	position: string
	pay: string
	date: string
}

export function CardVaga(props: CardProps) {
	return (
		<Link href={'/vagas/' + props.id}>
			<div className={styles.card}>
				<div className={styles.header}>
					<div className={styles.logo}>
						<IoBusiness />
					</div>
					<div className={styles.info}>
						<div className={styles.title}>{props.title}</div>
						<div className={styles.subtitle}>{props.company}</div>
					</div>
				</div>

				<div className={styles.description}>
					<div className={styles.info1}>
						<div>Área: {props.field}</div>
						<div>Posição: {props.position}</div>
					</div>
					<div className={styles.info2}>
						<div className={styles.icon}>
							<FaCalendarAlt />
							<div className={styles.info}>Até 10/10/2021</div>
						</div>
						<div className={styles.downicons}>
							<div className={styles.icon}>
								<FaMapMarkerAlt />
								<div className={styles.info}>Remoto</div>
							</div>
							<div className={styles.icon} id={styles.money}>
								<FaRegMoneyBillAlt />
								<div className={styles.info}>{props.pay}</div>
							</div>
						</div>
					</div>
				</div>

				<div className={styles.footer}>
					<div className={styles.info}>
						Por <span>CEE</span>
					</div>
				</div>
			</div>
		</Link>
	)
}
